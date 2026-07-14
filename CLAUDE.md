# Bowling

## 작업 방식

이 프로젝트는 TDD(Test-Driven Development) 기반으로 볼링 점수 계산 로직을 작성한다.
사이클은 Red -> Green -> Refactor가 아니라 **RED -> GREEN -> REVIEW**이며, human-in-the-loop로 진행한다.

- 한 번에 여러 기능을 구현하지 않고, 작은 단위의 RED-GREEN-REVIEW 사이클을 반복한다.
- 구체적인 규칙, 코딩 컨벤션은 `tdd-skill` 스킬(`.claude/skills/tdd-skill/SKILL.md`)을 따른다.

### 사이클별 작업 순서

1. **RED**
   - 다음에 구현할 실패하는 테스트에 대한 계획을 `Plan.md`에 작성한다.
   - 실패하는 테스트를 작성하고, 실제로 실패하는지 확인한다.
   - `Plan.md` 갱신 + 실패 테스트를 하나의 커밋으로 commit한다.
2. **GREEN**
   - 테스트를 통과시키는 최소한의 코드를 구현한다.
   - 전체 테스트가 통과하는지 확인한다. (이 단계에서는 commit하지 않는다.)
3. **REVIEW**
   - 구현된 코드를 사용자(나)에게 보여주고 검토를 받는다.
   - 수정 요청이 있으면 반영 후 다시 테스트 통과를 확인하고 재검토받는다.
   - 승인이 떨어지면 그제서야 GREEN 구현을 commit한다.
   - 승인 없이는 절대 commit하지 않는다.

즉, 한 사이클당 최소 2번의 commit이 생긴다: (1) RED 단계의 `Plan.md` + 실패 테스트, (2) REVIEW 승인 후의 GREEN 구현.
