from path import Path
import wandb

from imind.globals.ipaths import PCRelativeEnvConfig

# Method 01: Set env variable
# Ref: https://docs.wandb.ai/guides/track/advanced/environment-variables
# ----------------------------
# import os
# os.environ["WANDB_MODE"]="offline"

# Method 02
# ----------------------------------------------------------------------------
# Create a setting file or modify the exsting setting file which can be set in 
# env variable: WANDB_CONFIG_DIR
# This defaults to ~/.config/wandb, 
# you can override this location with this environment variable

def test_run(name, dir):
    
    # Method 03: Pass settings dictionary to `wandb.init(..., settings = {"mode" : "offline"})`
    wandb.init(project="test-project", entity="imindlabs", name=name, dir=dir)
        
    wandb.config = {
        "learning_rate": 0.001,
        "epochs": 100,
        "batch_size": 128
    }
    
    wandb.log({"loss": 50})
    wandb.log({"loss": 100})
    wandb.log({"loss": 110})
    wandb.log({"loss": 115})
    wandb.log({"loss": 150})
    wandb.log({"loss": 200})
    print("CONFIG:", wandb.config)

    # At the end of your script, we will automatically call `wandb.finish` to
    # finalize and cleanup the run. However, if you call `wandb.init` from a
    # child process, you must explicitly call `wandb.finish` at the end of the
    # child process.
    wandb.finish()
    
test_run("test-run-103", Path(PCRelativeEnvConfig.get_path("DLN_PATH"))/"tutorials"/"03_wandb")


# Once offline files are saved, you can sync the file using 
# wandb sync <path to run folder>

# Also, to 