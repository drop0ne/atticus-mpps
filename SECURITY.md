# Security Policy

ATTICUS MPPS is an early environmental perception prototype.

## Scope

Security issues include:

- unsafe file handling
- path traversal
- packet tampering
- replay/log integrity defects
- unintended retention of sensitive data
- governance bypasses
- addition of prohibited surveillance analytics

## Out-of-Scope for v0.1

- outdoor deployment hardening
- network service exposure
- cloud-hosted telemetry
- production authentication/authorization

## Reporting

For now, open a GitHub issue with the `security` label if the issue is not sensitive.

For sensitive issues, do not post exploit details publicly. Contact the repository owner directly.

## Safety Boundary

This project must not add person identification, face recognition, license-plate recognition, vehicle tracking, or other identity analytics.
