## Flask Clean Console

With some extra code any Flask app can be made to have
a clean console log that can be improved further.

The console log will look like this:

```
10.1.1.10   2022-09-18 20:03:11   0.104   /
10.1.1.10   2022-09-18 20:03:11   0.151   /contact
10.1.1.10   2022-09-18 20:03:12   0.107   /
10.1.1.10   2022-09-18 20:03:12   0.152   /contact
10.1.1.10   2022-09-18 20:03:13   0.108   /
10.1.1.10   2022-09-18 20:03:13   0.164   /contact
```


It will output **IP**, **TimeStamp**, **Duration** and **Requested Path**.

Please check comments in cfg file and main file to understand how
it is working and to tweak settings.
