## TEST_FRONT_END

Test the front end of the app.

--- 
description: closed loop frontend test - runs and fixes tests.

- spin and spin until all tests pass.
---

### test fe (closed loop)

run frontend tests and fix failures automatically.

#### closed loop pattern

### 1. REQUEST
run the front end test suite.

### 3. validate
```bash
uv run .claude/test_fe.md
npm run test
```

### 3. resolve 
if tests fails:
- read the fail test output
- fix the component or test
- return to step 2

loop exits when all tests pass.