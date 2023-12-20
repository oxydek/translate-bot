It looks like the problem comes from the Googletrans library that gets installed by default when you use pip install googletrans. This is because it uses an outdated version of the httpcore library.

You need to reinstall googletrans and httpcore libraries with the specific versions that work together.

Here is what you should do:

- Uninstall the existing googletrans and httpcore library.

pip uninstall googletrans httpcore


- Install an older, compatible version of httpcore and the newest version of googletrans.

pip install httpcore==0.9.1 googletrans==4.0.0-rc1


This should solve your problem. You can check the installation of the correct versions by running pip show googletrans and pip show httpcore. You should see the versions set at 4.0.0rc1 for googletrans and 0.9.1 for httpcore. 

Afterward, you should be able to run your script again. There won't be conflicts with the SyncHTTPTransport attribute since it is only available in httpcore version 0.10.0 and later.
