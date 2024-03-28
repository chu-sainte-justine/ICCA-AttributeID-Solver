
import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Define the SQLAlchemy base
Base = declarative_base()

# Define the d_attribute table model
class DAttribute(Base):
    __tablename__ = 'd_attribute'

    attributeid = Column(Integer, primary_key=True)
    longlabel = Column(String)

# Connection details
db_url = 'postgresql://username:password@server:port/database'

# Create an engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Function to find longlabel for attributeId
def find_longlabel(attributeId):
    return session.query(DAttribute.longlabel).filter(DAttribute.attributeid == attributeId).scalar()

# Function to find attributeIds for a given longlabel
def find_attributeIds(longlabel):
    return [row[0] for row in session.query(DAttribute.attributeid).filter(DAttribute.longlabel.like(longlabel)).all()]

# Main function
def main():
    # Read attributeIds from CSV file
    attributeIds = []
    with open("unique_values.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            attributeIds.append(int(row[0]))

    # Dictionary to store results
    results = {}

    # Iterate over attributeIds
    for attributeId in attributeIds:
        longlabel = find_longlabel(attributeId)
        if longlabel:
            matching_attributeIds = find_attributeIds(longlabel)
            if longlabel not in results:
                results[longlabel] = matching_attributeIds
            else:
                results[longlabel].extend(matching_attributeIds)

    # Write results to CSV file
    with open("label_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Longlabel", "Matching AttributeIds"])
        for longlabel, attributeIds in results.items():
            writer.writerow([longlabel, attributeIds])

if __name__ == "__main__":
    main()
