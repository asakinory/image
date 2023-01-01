def start(args, hkubeapi):
    input = args['input'][0]
    if input and input["action"] == "start_alg":
        ret = hkubeapi.start_algorithm("my-alg", [7], includeResult=True)
        return ret

    if input and input["action"] == "start_stored_subpipeline":
        ret = hkubeapi.start_stored_subpipeline("simple", {"files": {"link": "links-1"}}, includeResult=True)
        return ret

    if input and input["action"] == "start_raw_subpipeline":
        subPipeOp = {
            "batchTolerance": "100",
            "concurrentPipelines": {
                "amount": "10",
                "rejectOnFailure": "true"
            },
            "progressVerbosityLevel": "info",
            "ttl": "3600"
        }
        flowInput = {
            "files": {
                "link": "links-1"
            }
        }
        nodes = [{"nodeName": "one",
                    "algorithmName": "green-alg",
                    "input": []},
                    {"nodeName": "two",
                    "algorithmName": "black-alg",
                    "input": ["@one"]}]
        ret = hkubeapi.start_raw_subpipeline("raw-sub-pipeline", nodes, flowInput, options=subPipeOp, webhooks={},
                                                includeResult=True)
        return ret

    return 42



