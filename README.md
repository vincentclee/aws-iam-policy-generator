# aws-iam-policy-generator
NOFORN Presents: AWS IAM Policy Generator

## generator.py
python script to generate minified AWS IAM policies from a list of all known IAM actions

### Requirements
* Python >= 3.7

### The IAM actions list
It's one action per line, plain text format: `files/all-actions.txt`

The base reference list is sourced from: [rvedotrc/aws-iam-reference](https://github.com/rvedotrc/aws-iam-reference)

## Why?
You can add as many inline policies as you want to an IAM user, role, or group. But the total aggregate policy size (the sum size of all inline policies) per entity cannot exceed the following limits:

  * User policy size cannot exceed 2,048 characters.
  * Role policy size cannot exceed 10,240 characters.
  * Group policy size cannot exceed 5,120 characters.

Note: IAM does not count white space when calculating the size of a policy against these limitations.

### Usage
```
./generator.py --help
usage: generator.py [-h] -s SERVICES

NOFORN Presents: AWS IAM Policy Generator

optional arguments:
  -h, --help            show this help message and exit
  -s SERVICES, --services SERVICES
                        The command separated list of AWS Services by their
                        service prefix.
```

### Example
#### One Service
```
./generator.py -s ec2
Great Success
AWS IAM policy generated: policy.json
```

#### Two or More Services
```
./generator.py -s ec2,s3
Great Success
AWS IAM policy generated: policy.json
```

### Troubleshooting
Error: IAM Actions are missing for the service

```
./generator.py -s ec3
Error: IAM Actions are missing for the service: ec3
Traceback (most recent call last):
  File "./generator.py", line 46, in <module>
    _actions = sorted(actions[service])
KeyError: 'ec3'
```

Resolution: Add missing IAM Actions to `files/all-actions.txt` and re-run the generator.

## References
* [rvedotrc/aws-iam-reference](https://github.com/rvedotrc/aws-iam-reference) (all-actions.txt)
* [Actions, Resources, and Condition Keys for AWS Services - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html)
* [IAM and STS Limits - AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html)
