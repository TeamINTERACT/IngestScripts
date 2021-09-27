These Jupyter Notebook scripts are used to manage the telemetry ingest cycle for the INTERACT research project. The notebook for Ethica is distinct from the SenseDoc notebook, because that data comes in different forms, but they both follow the same basic workflow.

## History
Since ingesting involves working with the ground-truth data, which is messy, fragile, and crucial to the mission, the process is structured as an essentially manual one. This ensures that the ingest operator is paying full attention to the data and the steps of the process, and can respond appropriately if any new wrinkles arise.

Early versions of the ingest process were entirely manual, driven by single-purpose scripts as we learned the parameters and limitations of the incoming data. As that was an evolving, experimental process, the documentation was sparse and constantly being superseded by newer methods and scripts.

Once the process had matured, we then amalgamated those scripts and procedures into these Jupyter Notebooks, so that the process became self-contained and could be properly explained and documented.

Any attempt to automate this process further is strongly discouraged.

## Guide
  1. For a new ingest cycle, work your way through the relevant Jupyter Notebook.
  2. Begin by ensuring that the initial parameters in the first code block have been set up properly.
  3. Proceed through each block, reading the notes and then executing the code that follows.
  4. The process is serial, so for any given code block, it is crucial that all previous blocks have been run successfully, to completion.
  5. Be aware that in-memory variables created in one block are often used again later, so if any block produces errors, fix them, and then begin the process again from the top, to ensure that all in-memory variables are consistent throughout the entire run. 
  6. Once a particular ingest is complete and verified, create a PDF snapshot of the results by running:
    `jupyter nbconvert Ingest-Ethica-Van-W1.ipynb --to pdf --output IngestReport-Ethica-Van-W1-20201007.pdf`
  7. After producing the PDF report, if any changes were made to the code or to the documentation during this run, clear all output cells, save the Jupyter Notebook to disk, and then commit the changes to the git repo.

