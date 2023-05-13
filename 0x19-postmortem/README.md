# Postmortem: Slow Page Loading Times on E-commerce Website

## Issue Summary

On May 10, 2023, our e-commerce website experienced slow page loading times and intermittent timeouts from 3:00 PM to 5:00 PM EST. Roughly 25% of our users were affected, resulting in missed sales opportunities and unhappy customers.

## Timeline

- 3:00 PM: A monitoring alert signaled an issue with our website.
- 3:05 PM: Our engineers began investigating the issue in the web server logs.
- 3:15 PM: Initial assumption was that the issue was due to high traffic volume, so server capacity was increased.
- 3:30 PM: Issue was identified as a slow-moving database, not related to server capacity.
- 4:00 PM: Optimizing database queries was attempted but did not resolve the issue.
- 4:30 PM: Issue was escalated to senior engineering team for further investigation.
- 5:00 PM: Root cause was identified as a misconfigured database causing slow query execution, and was fixed.

## Root Cause and Resolution

The root cause of the issue was a misconfigured database that was using an outdated query optimizer, leading to slow query execution. To fix the issue, the query optimizer was updated, queries were optimized, and the database configuration was updated to prevent similar issues in the future.

## Corrective and Preventative Measures

To prevent a similar issue from occurring in the future, the following measures will be implemented:

- Regular monitoring and alerting for slow page loading times and high response times
- Regular review and update of database configurations
- Regular database maintenance, including software updates and query optimizations
- Review and update of incident response procedures

## Tasks to Address the Issue

1. Update the database configuration to use modern query optimizers
2. Optimize queries to improve database performance
3. Conduct regular database maintenance to update software and optimize queries
4. Review and update incident response procedures

In conclusion, the slow page loading times on our e-commerce website on May 10, 2023, were caused by a misconfigured database using an outdated query optimizer. Our engineers were able to identify and fix the root cause of the issue, and preventative measures will be taken to ensure a similar issue does not occur in the future.
