from hd import HD_Key
import unittest


class TestHD(unittest.TestCase):
    # Made using test vectors from BIP 32
    def test_parse_xprv1(self):
        s = "xprv9s21ZrQH143K2MPKHPWh91wRxLKehoCNsRrwizj2xNaj9zD5SHMNiHJesDEYgJAavgNE1fDWLgYNneHeSA8oVeVXVYomhP1wxdzZtKsLJbc"
        nk = HD_Key.parse_priv(s)
        self.assertEqual(nk.level, "00")
        self.assertEqual(nk.fingerprint, "00000000")
        self.assertEqual(nk.index,"00000000")
        self.assertEqual(nk.k, "081549973bafbba825b31bcc402a3c4ed8e3185c2f3a31c75e55f423e9629aa3")
        self.assertEqual(nk.c, "1d7d2a4c940be028b945302ad79dd2ce2afe5ed55e1a2937a5af57f8401e73dd")

    def test_parse_xprv2(self):
        s = "xprv9z4pot5VBttmtdRTWfWQmoH1taj2axGVzFqSb8C9xaxKymcFzXBDptWmT7FwuEzG3ryjH4ktypQSAewRiNMjANTtpgP4mLTj34bhnZX7UiM"

        nk = HD_Key.parse_priv(s)
        self.assertEqual(nk.fingerprint, "bef5a2f9")
        self.assertEqual(nk.index, "80000002")
        self.assertEqual(nk.k, "cbce0d719ecf7431d88e6a89fa1483e02e35092af60c042b1df2ff59fa424dca")
        self.assertEqual(nk.c, "04466b9cc8e161e966409ca52986c584f07e9dc81f735db683c3ff6ec7b1503f")
    
    def test_parse_xprv3(self):
        s = "xprv9xJocDuwtYCMNAo3Zw76WENQeAS6WGXQ55RCy7tDJ8oALr4FWkuVoHJeHVAcAqiZLE7Je3vZJHxspZdFHfnBEjHqU5hG1Jaj32dVoS6XLT1"
        nk = HD_Key.parse_priv(s)
        self.assertEqual(nk.fingerprint, "cfa61281")
        self.assertEqual(nk.index, "80000001")
        self.assertEqual(nk.k, "3a2086edd7d9df86c3487a5905a1712a9aa664bce8cc268141e07549eaa8661d")
        self.assertEqual(nk.c, "a48ee6674c5264a237703fd383bccd9fad4d9378ac98ab05e6e7029b06360c0d")
    
    def test_serialize1(self):
        want = "xprvA2nrNbFZABcdryreWet9Ea4LvTJcGsqrMzxHx98MMrotbir7yrKCEXw7nadnHM8Dq38EGfSh6dqA9QWTyefMLEcBYJUuekgW4BYPJcr9E7j"
        new_key = HD_Key("05", "31a507b8", "00000002", "bb7d39bdb83ecf58f2fd82b6d918341cbef428661ef01ab97c28a4842125ac23", "9452b549be8cea3ecb7a84bec10dcfd94afe4d129ebfd3b3cb58eedf394ed271")
        self.assertEqual(new_key.serialize(priv=True), want)

    def test_serialize2(self):
        want = "xprv9uPDJpEQgRQfDcW7BkF7eTya6RPxXeJCqCJGHuCJ4GiRVLzkTXBAJMu2qaMWPrS7AANYqdq6vcBcBUdJCVVFceUvJFjaPdGZ2y9WACViL4L"
        new_key = HD_Key("01", "41d63b50", "80000000", "491f7a2eebc7b57028e0d3faa0acda02e75c33b03c48fb288c41e2ea44e1daef", "e5fea12a97b927fc9dc3d2cb0d1ea1cf50aa5a1fdc1f933e8906bb38df3377bd")
        self.assertEqual(new_key.serialize(priv=True), want)
    
    def test_serialize3(self):
        want = "xpub69H7F5d8KSRgmmdJg2KhpAK8SR3DjMwAdkxj3ZuxV27CprR9LgpeyGmXUbC6wb7ERfvrnKZjXoUmmDznezpbZb7ap6r1D3tgFxHmwMkQTPH"
        new_key = HD_Key.parse_priv("xprv9vHkqa6EV4sPZHYqZznhT2NPtPCjKuDKGY38FBWLvgaDx45zo9WQRUT3dKYnjwih2yJD9mkrocEZXo1ex8G81dwSM1fwqWpWkeS3v86pgKt")
        self.assertEqual(new_key.serialize(), want)

    def test_serialize4(self):
        want = "xpub6BJA1jSqiukeaesWfxe6sNK9CCGaujFFSJLomWHprUL9DePQ4JDkM5d88n49sMGJxrhpjazuXYWdMf17C9T5XnxkopaeS7jGk1GyyVziaMt"
        new_key = HD_Key.parse_priv("xprv9xJocDuwtYCMNAo3Zw76WENQeAS6WGXQ55RCy7tDJ8oALr4FWkuVoHJeHVAcAqiZLE7Je3vZJHxspZdFHfnBEjHqU5hG1Jaj32dVoS6XLT1")
        self.assertEqual(new_key.serialize(), want)
    
    def test_create_master1(self):
        my_seed = bytes.fromhex("fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542")
        new_key = HD_Key.new_master_key("00", "00000000", "00000000", my_seed)
        want = "xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U"
        self.assertEqual(new_key.serialize(priv=True), want)
    
    def test_create_master2(self):
        my_seed = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
        new_key = HD_Key.new_master_key("00", "00000000", "00000000", my_seed)
        want = "xprv9s21ZrQH143K3QTDL4LXw2F7HEK3wJUD2nW2nRk4stbPy6cq3jPPqjiChkVvvNKmPGJxWUtg6LnF5kejMRNNU3TGtRBeJgk33yuGBxrMPHi"
        self.assertEqual(new_key.serialize(priv=True), want)
    
    def test_CKDpriv1(self):
        want = "xprv9vHkqa6EV4sPZHYqZznhT2NPtPCjKuDKGY38FBWLvgaDx45zo9WQRUT3dKYnjwih2yJD9mkrocEZXo1ex8G81dwSM1fwqWpWkeS3v86pgKt"
        want = HD_Key.parse_priv(want)

        prev = bytes.fromhex("fffcf9f6f3f0edeae7e4e1dedbd8d5d2cfccc9c6c3c0bdbab7b4b1aeaba8a5a29f9c999693908d8a8784817e7b7875726f6c696663605d5a5754514e4b484542")
        key = HD_Key.new_master_key("00", "00000000", "00000000", prev)
        ck = key.CKDpriv(0)

        self.assertEqual(want.level, ck.level)
        self.assertEqual(want.fingerprint, ck.fingerprint)
        self.assertEqual(want.index, ck.index)
        self.assertEqual(want.k, ck.k)
        self.assertEqual(want.c, ck.c)

    def test_CKDpriv2(self):
        prev = HD_Key.parse_priv("xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U")
        ck = prev.CKDpriv(1)
        want = "xprv9vHkqa6EV4sPZSpU25dGFR6ySsAhKJHg21b2b6PhJb3EUMJcz77ukS7SmyJuQbm6V2bAZ5y1kXmpuPRS7mkfQFNNhDFeoxk4B67f3uYBaSo"
        self.assertEqual(ck.serialize(priv=True), want)

    def test_CKDPriv3(self):
        prev = HD_Key.parse_priv("xprv9s21ZrQH143K25QhxbucbDDuQ4naNntJRi4KUfWT7xo4EKsHt2QJDu7KXp1A3u7Bi1j8ph3EGsZ9Xvz9dGuVrtHHs7pXeTzjuxBrCmmhgC6")
        ck = prev.CKDpriv(10)
        want = "xprv9uPDJpEGLkshUCWRN3Lc8hhgvnoTwG1VFoD2JEzQy9NMP4YPoaMXHwrei1iyUdZEYc8RzkaX74GH7U6uUKKqC2kCFUzw3yTB8ncL7yvUQrg"
        self.assertEqual(ck.serialize(priv=True), want)

    def test_CKDpriv4(self):
        prev = HD_Key.parse_priv("xprv9s21ZrQH143K31xYSDQpPDxsXRTUcvj2iNHm5NUtrGiGG5e2DtALGdso3pGz6ssrdK4PFmM8NSpSBHNqPqm55Qn3LqFtT2emdEXVYsCzC2U")
        ck = prev.CKDpriv(2)
        want = "xprv9vHkqa6EV4sPcjMMuDToT9SVa6UHCwR4pxvYKZdKTqWpcgQqmPuphAbteLtH9GTXaB87d9zYGuVN497UHmPB462kDjovoB7YoYXYKYphJVv"
        self.assertEqual(ck.serialize(priv=True), want)

if __name__ == '__main__':
    unittest.main()
