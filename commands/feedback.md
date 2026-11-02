---
description: File feedback as a ticket in POC Build Loop (FB-<n>) — about a POC, a one-off asset or POC Studio in general — or check a ticket's status
argument-hint: [status FB-<n>] | [skill or stage] <your feedback>
---

Feedback for POC Studio: **$ARGUMENTS**

Every piece of feedback becomes a ticket (`FB-<n>`) on POC Build Loop's Feedback page
(https://poc-build-loop-orbit.tensor-uat.unifyapps.com/feedback), where people triage it (assignee, priority, status).
It is not a change request on one document (a change request on a document stays an Iteration, written by the
orbit-writeback skill at that gate). A POC is optional: feedback from a one-off asset run, or about POC Studio in
general, is filed too.

1. **Status check.** If the text above is `status FB-<n>`, `status <n>`, `fb <n>`, `FB-<n>` or just a number, it is a
   read only: load the `orbit-writeback` skill (Skill tool: `poc-studio:orbit-writeback`), follow its
   **Ticket status** subsection under `/feedback`, and stop. Write nothing.
2. If no feedback text was given above, ask for it in one short question ("What feedback should I file?") and wait.
3. Load the `orbit-writeback` skill (Skill tool: `poc-studio:orbit-writeback`) and follow its **`/feedback`** section
   exactly. It uses the same UnifyApps Headless tenant tools and the same write rules as every other Orbit write: one
   ticket on `orbit_studio_feedback`, then one `created` row on `orbit_studio_feedback_event`.
4. The ticket carries a `skill` field: the skill or agent the feedback is about (named by the person, or decided from
   the text and this session), or `general` when it could be several or none fits — as the `/feedback` section says.
5. **Reply in one line:**
   `Logged FB-<seq> for <client, or General>, under <skill name or General>. Track it: https://poc-build-loop-orbit.tensor-uat.unifyapps.com/feedback/FB-<seq>`
   If the write fails, show the error in one line and what to do.
6. **Nothing else.** No Iteration row, no Activity row on the POC, no POC update, no `slack_notification`, no Slack
   message: feedback does not move a POC. Never set an assignee, due date, tags or analysis fields, and never update
   or delete a ticket; people do that in the app.
