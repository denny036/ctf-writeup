![alt text](image.png)

We are given a `logs.txt` file.

Upon analyzing this file, I got a suspicious endpoint:

![alt text](image-1.png)

`/admin/ufile.io/y8ls94tu`

Then, I removed the `admin` part and accessing the site.

![alt text](image-2.png)

As we can see, we got Admin.zip that we could download. After downloaded the file, we got 5 CSV files inside the archive file:

![alt text](image-3.png)

Analyzing file by file, I got the flag inside the `users.csv` file. It has 61 lines and the flag is on 21th line.

![alt text](image-4.png)

flag: texsaw{g0tcha_fl@g_m1ne}

