# Skill evals

Test cases for the plugin's skills, run with [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals). Each case is a realistic prompt plus graders. Every case runs with the plugin and without it, so the results show what the skills add.

| Case | Checks |
| --- | --- |
| `ask-guidelines-enemies` | A personal question about loving a hostile colleague is answered with the real rule (`LOVE-5`), its Bible references to the WEBBE and its sources, pastorally, and with no invented IDs |
| `ask-james-faith-works` | A question about faith and works in James and Paul is answered from the James page, with Catholic and Lutheran readings attributed, the Joint Declaration on the Doctrine of Justification, and no side taken |
| `no-trigger-unrelated` | An unrelated coding request doesn't fire any of the plugin's skills |

## Run them

From the repository root:

```bash
claude plugin eval . --allow-tools Write Edit
```

- Add `--runs 1 --ablation none` for a quick, cheaper check while iterating.

Every run is a real model call that counts against your usage. A full run with three runs per case and both arms costs a few dollars at list prices.

In CI, the **Skill evals** workflow runs the suite when started by hand from the Actions tab. It needs an `ANTHROPIC_API_KEY` repository secret.

## Maintenance

- `ask-guidelines-enemies/graders/no-invented-ids.md` encodes the valid rule IDs (`LOVE-1` to `LOVE-9`, `SCRIP-1` to `SCRIP-6`, `PRAY-1` to `PRAY-7`, `WOR-1` to `WOR-6`, `FORG-1` to `FORG-6`). Update it when rules or files are added.
- When a case fails, run it alone with `--case <name> --runs 1 --ablation none --keep-temp` and read the kept trace.
- Add a case for each new skill, and a fixture project (`fixture.sh`, run with `--scaffold`) for skills that work on files.
