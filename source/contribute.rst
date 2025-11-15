Contribute
==========

We welcome contributions to the Judge0 documentation! Whether you're fixing typos, adding new content, or improving existing sections, your help is greatly appreciated.

Instructions
------------

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

6. Start a live preview server to see your changes in real-time.

   .. code-block:: bash

      uv run make livehtml

7. Open your web browser and navigate to `http://localhost:8000 <http://localhost:8000>`_ to view the documentation.
8. Commit and push your changes to your forked repository.
9. Create a pull request to the main repository.

Adding Packages
---------------

To add a new package, use the following command:

.. code-block:: bash

    uv add <package-name> # e.g. uv add sphinx-autobuild
