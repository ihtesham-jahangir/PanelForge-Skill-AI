# Frontend Engineering

For new web applications, use Next.js with React and TypeScript, styled with
responsive, reusable, accessible Tailwind CSS components. Keep this frontend
as a separate application that consumes documented REST APIs from FastAPI;
never place business logic, authentication decisions, authorization, or
database operations only in the browser.

Organize features around user workflows and server contracts. Keep loading, error, empty, optimistic, disabled, and permission states explicit. Use the existing component and token system, accessible semantics, keyboard navigation, resilient network handling, and responsive layouts. Never treat client-side route guards or hidden controls as authorization.
