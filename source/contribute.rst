Contribute
==========

1. Install `uv <https://docs.astral.sh/uv/getting-started/installation>`_.
2. Fork the repository on `GitHub <https://github.com/judge0/docs/fork>`_.
3. Clone your forked repository.
4. Navigate to the ``docs`` directory and install the dependencies.

   .. code-block:: bash

      cd docs
      uv sync

5. Add your content using ``reStructuredText`` syntax. See the `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ documentation for details or any of the following resources:

   - `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`_
   - `Quick reStructuredText <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_
   - `The reStructuredText_ Cheat Sheet: Syntax Reminders <https://docutils.sourceforge.io/docs/user/rst/cheatsheet.rst>`_

6. Build your changes locally.

   .. code-block:: bash

      rm -rf build; uv run make html

7. Open the generated HTML files (``./build/html/index.html``) in your browser to review your changes.
8.  Commit and push your changes to your forked repository.
9. Create a pull request to the main repository.
