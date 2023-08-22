from watchdir import Watcher


def test_symlink_dir_removal_handled_correctly(tmp_path):
    # Create a symlink to a folder with files
    hard = tmp_path / "hard_path"
    hard.mkdir()
    (hard / "a_file").touch()
    (tmp_path / "link_path").symlink_to(hard)
    elapsed_time = 0
    # Time it out and ensure that it doesn't crash
    watcher = Watcher(tmp_path, clock=lambda: elapsed_time, timeout=1)
    watcher.scan()
    elapsed_time += 2
    watcher.scan()
