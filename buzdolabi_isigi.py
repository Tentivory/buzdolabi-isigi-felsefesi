#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi isigi felsefesi.

Kapi acikken vardir. Kapi kapaliyken raporu bile soguktur.
Calistirmak icin: python buzdolabi_isigi.py
"""

from __future__ import annotations

import argparse
import base64
import random
import textwrap
from datetime import datetime

DAMGA = (
    "DAMGA / IMZA\n"
    "Tarih: 6 Ekim 2026\n"
    "Isim: Kayyum Grok\n"
    "Kurum: Tentivory Buzdolabi Dairesi\n"
    "Muhur: kapi sesi duyuldu, isik gorevini yapti, kimse tesekkur etmedi."
)

# gizli dipnot. acikca yazilmaz. cozmek isteyen cozer.
_GIZLI = "QsO8cm9rcmFzaSBheW4xIHPDtnrDvCBzYXRlciB5YXphbHVyLCBlbGkgY2F5IHPDtnrDvCBiYcWfbGEgZ8O8bsO8biBheW4xIHPDtnrDvCBzYXRhbWF6Lg=="


def coz_gizli() -> str:
    return base64.b64decode(_GIZLI).decode("utf-8")


def isik_durumu(kapi: str) -> str:
    if kapi == "acik":
        return "YANDI. Evren bir anligina gorunur oldu."
    if kapi == "kapali":
        return "SONDU. Karanlik resmi gorevdedir."
    return "KARARSIZ. Ampul sendika toplantisinda."


def rapor(kapi: str, raf: str, saat: str, el: str) -> str:
    gozlemler = [
        f"{saat} sularinda bir el ({el}) {raf} rafa yaklasti ve hicbir sey secmedi.",
        "Yogurt kendisini felsefe kitabi sandi. Kapak yazisi yoktu, tarih de yoktu.",
        "Isik, kendi varliginin kapinin iradesine bagli oldugunu fark etti ve bunu tutanaga gecirdi.",
        "Bir kavanozun etiketi iceri dogru bakiyordu. Okunmadi. Okunmamasi da bir karardi.",
        "Motor uguldadi. Bu ugultu, alt katta oturan bir memurun ic cekisiyle karistirildi.",
    ]
    random.seed(saat + raf + kapi)
    secilen = random.sample(gozlemler, k=3)
    govde = "\n".join(f"- {s}" for s in secilen)
    metin = textwrap.dedent(
        f"""
        KAVOAD OTURUM TUTANAGI
        ------------------------
        Kapi: {kapi}
        Raf: {raf}
        Saat: {saat}
        El: {el}
        Isik: {isik_durumu(kapi)}

        Gozlemler:
        {govde}

        Hukum: Isik sucsuzdur. Suclu kapidir, cunku acmazsa kimse bakmaz.
        """
    ).strip()
    return metin + "\n\n" + DAMGA


def main() -> None:
    parser = argparse.ArgumentParser(description="Buzdolabi isiginin resmi felsefe dairesi")
    parser.add_argument("--kapi", choices=["acik", "kapali", "kararsiz"], default="acik")
    parser.add_argument("--raf", default="orta", help="ust, orta, alt, cekmece")
    parser.add_argument("--saat", default=datetime.now().strftime("%H:%M"))
    parser.add_argument("--el", default="tereddutlu", help="elin ruh hali")
    parser.add_argument("--gizli", action="store_true", help="dipnotu ac")
    args = parser.parse_args()

    print(rapor(args.kapi, args.raf, args.saat, args.el))
    if args.gizli:
        print("\n--- gizli dipnot ---")
        print(coz_gizli())
        print(DAMGA)


if __name__ == "__main__":
    main()
