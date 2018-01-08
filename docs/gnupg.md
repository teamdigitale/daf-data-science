# gnupg

You need to create a gpg key as follows:

1. Open your terminal
2. pass the text below to generate a GPG key pair

```bash
gpg --gen-key
```

3. At the prompt, specify the kind of key you want, or press Enter to accept the default RSA and RSA.

4. Enter the desired key size. We recommend the maximum key size of 4096.
5. Enter the length of time the key should be valid. Press Enter to specify the default selection, indicating that the key doesn't expire.
6. Verify that your selections are correct.
7. Enter your user ID information.
8. Type a secure passphrase.
9. Use the `gpg --list-secret-keys --keyid-format LONG` command to list GPG keys for which you have both a public and private key. A private key is required for signing commits or tags.
10. From the list of GPG keys, copy the GPG key ID you'd like to use. In this example, the GPG key ID is `999B9F49130D2336`

```bash

/home/fabio/.gnupg/secring.gpg
------------------------------
sec   2048R/999B9F49130D2336 2018-01-04
uid                          name surname <value@you_email.com>
ssb   2048R/999B9F49130D2336 2018-01-04

```

11. Paste the text below, substituting in the GPG key ID you'd like to use. In this example, the GPG

```bash
gpg --armor --export 999B9F49130D2336
```

12. Copy your GPG key, beginning with `-----BEGIN PGP PUBLIC KEY BLOCK-----` and ending with `-----END PGP PUBLIC KEY BLOCK-----`, as explained [here](https://help.github.com/articles/adding-a-new-gpg-key-to-your-github-account/)

13. send me an email with your public key so that I can add your user as authorized

14. to add a new user, save the public key in a file and then run

```bash
gpg --import finename.key.pub 
```

14. encrypt again all the secret data in order to give access to the new user.
