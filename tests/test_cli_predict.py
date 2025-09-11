import json, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]

def run_cli(args, stdin=None):
    cmd = [sys.executable, "-m", "ml.src.predict"] + args
    p = subprocess.run(
        cmd, input=(stdin or "").encode("utf-8"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        cwd=str(ROOT), check=True,
    )
    return json.loads(p.stdout.decode("utf-8"))

def test_cli_text_option():
    out = run_cli(["--text", "동화를 읽었다"])
    assert out["ok"] is True
    assert out["result"]["label"] in {"미술","신체","언어","과학","기타"}

def test_cli_stdin():
    out = run_cli([], stdin="자석을 관찰했다")
    assert out["ok"] is True
