# CRM Engineering

Core entities may include leads, contacts, companies, deals, pipelines, stages, activities, tasks, notes, attachments, tags, segments, scores, and reports. Create only the entities required by the business.

## Lifecycle

Define lead qualification and conversion, contact/company relationships, deal stage transitions, assignment rules, duplicate detection, follow-up scheduling, activity history, and ownership boundaries. Every transition should specify actor, allowed source states, validation, side effects, and audit event.

## Automation

Use `TRIGGER -> CONDITIONS -> ACTIONS`. Persist an execution ID, input snapshot, attempt count, status, timestamps, and error details. Actions must be idempotent, retried with bounded backoff where safe, and manually recoverable. Keep automation logs separate from user-facing activity history when their audiences differ.
