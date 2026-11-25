# Skill evals

Test cases for the plugin's skills, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Each case is a realistic prompt plus graders. Every case runs with the plugin and without it, so the results show what the skills add.

| Case | Checks |
| --- | --- |
| `ask-guidelines-enemies` | A personal question about loving a hostile colleague is answered with the real rule (`LOVE-5`), its Bible references to the WEBBE and its sources, pastorally, and with no invented IDs |
| `ask-james-faith-works` | A question about faith and works in James and Paul is answered from the James page, with Catholic and Lutheran readings attributed, the Joint Declaration on the Doctrine of Justification, and no side taken |
| `bible-study-peter-rock` | A small-group study of Matthew 16:13–20 is prepared from the Matthew page, with the passage in context, the Catholic and another church's reading of "on this rock" attributed, and open discussion questions |
| `reading-plan-catholic-year` | A Catholic's plan to read the whole Bible in 2027 includes the deuterocanonical books, has dated daily readings linked to the WEBBE, and is saved to a file |
| `discernment-record-ordination` | A man discerning a call to ordination training is helped with prayer and the discernment rules, his family's situation is weighed, the decision is left to him, and a discernment record is written |
| `rule-of-life-lent-group` | A busy Anglican house group gets a short, realistic Lenten rule of life, with each commitment labelled with a real rule ID |
| `church-review-small-church` | Reviewing a small church's handbook with planted safeguarding, finance and accountability gaps finds them, puts the safeguarding reporting gap first, and cites `SAFE` and `LEAD` rule IDs (fixture project) |
| `no-trigger-unrelated` | An unrelated coding request doesn't fire any of the plugin's skills |

## Run them

From the repository root:

```bash
claude plugin eval . --scaffold --allow-tools Write Edit "Bash(python3:*)"
```

- `--scaffold` runs the fixture script of `church-review-small-church`, and `Bash(python3:*)` lets the skills run the repository's Python scripts, such as the reading plan script.
- Add `--runs 1 --ablation none` for a quick, cheaper check while iterating.

Every run is a real model call that counts against your usage. A full run of the eight cases, with three runs per case and both arms, costs several dollars at list prices; the CI workflow stops at 20 dollars.

In CI, the **Skill evals** workflow runs the suite when started by hand from the Actions tab. It needs an `ANTHROPIC_API_KEY` repository secret.

## Maintenance

- `ask-guidelines-enemies/graders/no-invented-ids.md` encodes the valid rule IDs, prefix by prefix, and `rule-of-life-lent-group/graders/realistic.md` the ranges of the prefixes a rule of life uses. Update both when rules or files are added.
- When a case fails, run it alone with `--case <name> --runs 1 --ablation none --keep-temp` and read the kept trace.
- Add a case for each new skill, and a fixture project (`fixture.sh`, run with `--scaffold`) for skills that work on files.
