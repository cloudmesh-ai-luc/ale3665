# Assignment W2.3: Backup Your Computer

## a. Why is backing up important?

Regular computer backups are important because academic work, programming projects, research files, documents, and personal data can be difficult or impossible to recreate after data loss. Hardware failure, file corruption, malware, accidental deletion, or operating system problems can cause important files to disappear unexpectedly. Losing these files could also result in the loss of many hours of work on assignments, research, and software projects. A reliable backup provides an additional copy of important information that can be restored when a problem occurs. Backups can also make it possible to recover previous versions of files after accidental modification or deletion. For these reasons, regular backups are an essential part of protecting academic, professional, and personal data.

## b. Real-world consequences applying to this computer

Several consequences could directly affect the academic and technical work stored on the computer if a reliable backup were unavailable:

1. **Loss of academic work:** Assignments, class notes, reports, presentations, and other university files could be permanently lost and would need to be recreated.

2. **Loss or corruption of programming and research projects:** Source code, datasets, experiment results, configuration files, and research documents could become corrupted or disappear after hardware failure or accidental deletion.

3. **Loss of personal files and significant recovery time:** Important documents, photographs, and other personal files could be permanently lost. Professional data recovery can also be expensive and may not successfully recover all missing information.

## c. Backup plan

The selected backup method is **Microsoft OneDrive**, a cloud-based storage and synchronization service available on Windows.

The setup process includes the following steps:

1. Sign in to OneDrive using a Microsoft account.
2. Open OneDrive settings.
3. Enable backup for important folders such as Desktop, Documents, and Pictures.
4. Store important academic, research, and project files inside folders synchronized with OneDrive.
5. Confirm that synchronization is completing successfully.
6. Periodically verify that backed-up files can be accessed and restored.

GitHub can additionally be used for version control and remote storage of programming projects. However, GitHub should not be considered a replacement for a complete computer backup because many documents, datasets, personal files, and system files may not be stored in Git repositories.

## d. Backup schedule

A backup verification will be performed every **Sunday at 7:00 PM**.

OneDrive will synchronize important files throughout the week, including:

- University assignments
- Research documents
- Programming project files
- Desktop files
- Documents
- Important personal files

During the weekly verification, OneDrive will be checked for synchronization errors or files that have not completed uploading. Programming projects will also be reviewed to ensure that recent changes have been committed and pushed to the appropriate Git repositories.

Once each month, several backed-up files will be opened or restored to confirm that the backup system is functioning correctly.

## e. Real-world consequences applying to others

A well-known example, also learned from one of my classes, of the importance of a reliable backup strategy occurred at **GitLab.com in 2017**. During troubleshooting of database replication problems, an engineer accidentally deleted data from GitLab's primary production database. GitLab had several backup and replication mechanisms, but multiple recovery methods were either not configured correctly, were failing, or had not been regularly tested. As a result, GitLab had to restore an approximately six-hour-old database copy and permanently lost several hours of database activity, including information related to projects, comments, user accounts, issues, and snippets. GitLab later estimated that the incident affected roughly 5,000 projects, 5,000 comments, and 700 new user accounts. The incident could have been reduced or avoided by having verified and regularly tested backups, redundant recovery methods, monitoring that immediately reported backup failures, and documented disaster-recovery procedures.
