<!-- optional -->
![Name](http://gitlab.rete.farm/pepita/guideline/docs/raw/master/ReadmeRepository/images/immobiliare-labs.png)


<!-- required -->

# Signature Api

<!-- optional -->
[![pipeline status](http://gitlab.rete.farm/platform/core-data-services/signature_api/badges/develop/pipeline.svg)](http://gitlab.rete.farm/platform/core-data-services/signature_api/commits/develop)
[![coverage report](http://gitlab.rete.farm/platform/core-data-services/signature_api/badges/develop/coverage.svg)](http://gitlab.rete.farm/platform/core-data-services/signature_api/commits/develop)


<!-- required -->
FastApi App for digital signature procedures management, it exposes
custom routes wrapping external signature service provider apis.



<!-- required -->

## Table of Contents

- [Signature Api](#signature-api)
    - [Table of Contents](#table-of-contents)
    - [Documentation](#documentation)
    - [Requirements](#requirements)
    - [Where it is deployed](#where-it-is-deployed)
    - [Where to find the logs](#where-to-find-the-logs)
    - [Links](#links)
    - [Dependencies](#dependencies)
    - [Supported Devices](#supported-devices)
    - [Architectural Patterns](#architectural-patterns)
    - [Issues](#issues)
    - [Contributing](#contributing)
    - [How to deploy](#how-to-deploy)
    - [CI/CD](#cicd)
    - [Changelog](#changelog)
    - [Reference team](#reference-team)

<!-- optional -->

## Documentation

Signature Api routes docs can be found at `http://0.0.0.0:5000/docs` (
Swagger Openapi Specs)


<!-- required -->

## Requirements

- Python 3.7.8
- PIP + packages in `requirements.txt`

<!-- required -->

## Where it is deployed

| Environment   | Hostname                        | Link                        |
| :----------   | :-------                        | :---                        |
| Production    | `py0{1,4}.vrt.ext.rm.ns.farm`   | https://www.example.com     |
| Staging       | `py0{1,4}-staging.vrt.ext.rm.ns.farm` | https://staging.example.com |

<!-- required -->

## Where to find the logs

Where the different environments are logged

| Environment   | FastAPI Application Path            |
| :----------   | :---                                |
| Production    | `/var/log/signature_api.log`        |
| Staging       | `/var/log/signature_api.log`        |
| Dev Reference | `/var/log/signature_api.log`        |

<!-- required -->

## Links

| Name        | Link           |
| :---        | :---           |
| Metrics     | NULL           |
| Sentry      | NULL           |

<!-- optional -->

## Supported Devices

Any HTTP client


<!-- optional -->

## Architectural Patterns

A generic Model-View-Controller architecture


<!-- optional -->

## Issues

You can open an issue about this
project [here](http://gitlab.rete.farm/amarino/spiderman-scheduler/issues)


<!-- required -->

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md).


<!-- required -->

## How to deploy

Documentation on Ansible deployments
is [here](./ansible-deploy/README.md)

## CI/CD

Documentation on CI/CD configurations
is [here](./CONTRIBUTING.md#ci-structure)

<!-- optional -->

## Changelog

See [CHANGELOG](./CHANGELOG.md).


<!-- required -->

## Reference team

Python Team - Core Team
