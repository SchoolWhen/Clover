# Public Release Checklist

## Research identity

- [x] Highest research question is explicit.
- [x] Product goal is explicit.
- [x] Facts and hypotheses are separated.
- [x] Current status avoids scientific overclaim.
- [x] Roadmap is research-driven rather than version-driven.

## Repository

- [x] README and Chinese overview exist.
- [x] Principles, status, roadmap and contributing guides exist.
- [x] Apache-2.0 license is present.
- [x] Research decisions are tracked.
- [x] Research, hypothesis, architecture and evaluation documentation have defined homes.
- [ ] Existing Clover prototype code has been audited for public import.
- [ ] Build / test instructions are documented after code import.
- [ ] CI is configured after code import.

## Safety / hygiene before code import

- [ ] Search for API keys, tokens and credentials.
- [ ] Remove private URLs and local dataset locations.
- [ ] Remove personal absolute paths such as `file:///Users/...`.
- [ ] Review generated binaries and large artifacts.
- [ ] Verify public documentation links.

## Scientific claims

Before using strong terms such as `SOTA`, `solved`, `zero hallucination`, `fully understands`, or `AGI`, attach a reproducible public protocol and supporting result.
