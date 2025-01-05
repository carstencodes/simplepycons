#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class BankOfAmericaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bankofamerica"

    @property
    def original_file_name(self) -> "str":
        return "bankofamerica.svg"

    @property
    def title(self) -> "str":
        return "Bank of America"

    @property
    def primary_color(self) -> "str":
        return "#012169"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bank of America</title>
     <path d="M15.194 7.57c.487-.163 1.047-.307
 1.534-.451-1.408-.596-3.176-1.227-4.764-1.625-.253.073-1.01.271-1.534.434.541.162
 2.328.577 4.764 1.642zm-8.896 6.785c.577.343 1.19.812 1.786 1.209
 3.952-3.068 7.85-5.432
 12.127-6.767-.596-.307-1.119-.578-1.787-.902-2.562.65-6.947
 2.4-12.126 6.46zm-.758-6.46c-2.112.974-4.331 2.31-5.54
 3.085.433.199.866.361 1.461.65 2.671-1.805 4.764-2.905
 5.594-3.266-.595-.217-1.154-.361-1.515-.47zm8.066.234c-.686-.379-3.068-1.263-4.71-1.642-.487.18-1.173.451-1.642.65.595.162
 2.815.758 4.71 1.714.487-.235 1.173-.523 1.642-.722zm-3.374
 1.552c-.56-.27-1.173-.523-1.643-.74-1.425.704-3.284 1.769-5.63
 3.447.505.27 1.047.595 1.624.92 1.805-1.335 3.627-2.598
 5.649-3.627zm1.732 8.825c3.79-3.249 9.113-6.407 12.036-7.544a48.018
 48.018 0 00-1.949-1.155c-3.771 1.246-8.174 4.007-12.108 7.129.667.505
 1.371 1.028 2.02
 1.57zm2.851-.235h-.108l-.18-.27h-.109v.27h-.072v-.596h.27c.055 0 .109
 0 .145.036.054.019.072.073.072.127 0
 .108-.09.162-.198.162zm-.289-.343c.09 0 .199.018.199-.09
 0-.072-.072-.09-.144-.09h-.163v.18zm-.523.036c0-.289.235-.523.541-.523.307
 0 .542.234.542.523a.543.543 0 01-.542.542.532.532 0 01-.54-.542m.107
 0c0 .235.199.433.451.433a.424.424 0 100-.848c-.27 0-.45.199-.45.415"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
