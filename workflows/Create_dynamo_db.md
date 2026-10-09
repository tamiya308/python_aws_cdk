## Specs for
The setup of aws infrastructure & resources in the AWS cloud

## Objective
- Create dynamodb tables in the aws cloud using python & the aws cdk libraries via python code in this project. 
- Table Name: StudentEnrolments. PartitionKey: Id<number>, SortKey: Name<string>
- Typical json structure for reference purposes:
{
    "StudentId" : 1000,
    "StudentName" : "Alan Jones",
    "CourseName": "Commerce"
    "UnitsToComplete":[
        {
            "UnitId": 20,
            "UnitName": "Introduction to business",
        },
        {
            "UnitId": 21,
            "UnitName": "Managements basics"
        }
    ]
}

