"""Atalho para iniciar o sistema: python run.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from techflow.app import create_app  # noqa: E402

if __name__ == "__main__":
    create_app().run(debug=True)
