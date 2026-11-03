# Requirements and Acceptance Criteria

Convert each request into:

- Actor and business goal.
- User journey and affected resources.
- Functional behavior, including empty, loading, error, and retry states.
- Authorization and ownership rules.
- Data changes and migration needs.
- Accessibility and responsive requirements.
- Observable acceptance criteria.
- Unit, integration, API, and end-to-end verification.

Use explicit language such as “a member can update only records belonging to their organization” rather than UI-only descriptions. Flag unresolved business decisions instead of silently choosing behavior that can affect data or permissions.

Before implementation, run the [capability-gap preflight](../quality/capability-gaps.md)
for product terminology, roles, tenancy, retention, integrations, deployment,
and irreversible data operations. Record each answer, assumption, or
`requires-human-decision` state. The resulting capability matrix is part of the
acceptance criteria.
