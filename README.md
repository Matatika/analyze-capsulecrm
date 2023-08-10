# analyze-capsulecrm

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for Capsule

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-capsulecrm
  namespace: tap_capsulecrm
  update:
    analyze/datasets: true
  repo: https://github.com/Matatika/analyze-capsulecrm
  pip_url: git+https://github.com/Matatika/analyze-capsulecrm.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-capsulecrm

# Add the file bundle as a related plugin through adding the tap-capsulecrm extractor
meltano add extractor --include-related tap-capsulecrm
```
