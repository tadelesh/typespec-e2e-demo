# Adding additional specs or scenarios

To add additional specs for service codegen testing, please follow:

1. Create folder `/specifications/[SpecName]`.
1. Add TypeSpec files
1. Add `tspconfig.yaml` with desired emitter configuration. If you intend to have a runnable server under `/servers`, please add scaffolding code AND setup instructions in a `README.md`
1. Run `npx tsp compile .` to ensure no error in emitting service code.
1. Test and run server code to ensure the scenario is working correctly.
