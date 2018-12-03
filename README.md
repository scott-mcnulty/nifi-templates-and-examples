# NiFi Templates and Examples

Collection of NiFi templates and examples to get flows up and running quickly.

# Table of Contents
- [NiFi Templates and Examples](#nifi-templates-and-examples)
- [Table of Contents](#table-of-contents)
    - [Database Backfill](#database-backfill)
    - [Flatten Complex JSON Using JOLT](#flatten-complex-json-using-jolt)
    - [Load Balancing Demo](#load-balancing-demo)
    - [Sanitize Free Text Columns of CSV](#sanitize-free-text-columns-of-csv)

-----

## [Database Backfill](database-backfill/README.md)

Template to pull large amounts of data from database tables that contain time-stamped data. Good for pulling historical time series data and storing into a file system by day.

[to top](#nifi-templates-and-examples)

## [Flatten Complex JSON Using JOLT](flatten-complex-json-using-jolt/README.md)

Example of how I used [JOLT](https://jolt-demo.appspot.com/#inception) to flatten a complicated JSON object.

[to top](#nifi-templates-and-examples)

## [Load Balancing Demo](load-balancing-demo/README.md)

A demo showing how flowfiles can be spread across a NiFi cluster to balance compute load. Useful when wanting to distribute heavy computation between different nodes of the cluster.

[to top](#nifi-templates-and-examples)

## [Sanitize Free Text Columns of CSV](sanitize-free-text-columns-of-csv/README.md)

How I was able to sanitize newlines in a free text column in a csv using Jython. Jython was chosen because I wasn't able to intuatively use a regex along with a replaceText processor.

[to top](#nifi-templates-and-examples)