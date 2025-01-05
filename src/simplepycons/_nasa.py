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


class NasaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nasa"

    @property
    def original_file_name(self) -> "str":
        return "nasa.svg"

    @property
    def title(self) -> "str":
        return "NASA"

    @property
    def primary_color(self) -> "str":
        return "#E03C31"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NASA</title>
     <path d="M4.344 13.598c.075.281.195.39.407.39.22 0
 .335-.132.335-.39V8.804h1.379v4.794c0 .675-.088.968-.43
 1.31-.247.248-.703.439-1.278.439-.464
 0-.909-.154-1.192-.438-.249-.25-.386-.505-.599-1.311l-.846-3.196c-.074-.281-.194-.39-.406-.39-.22
 0-.336.132-.336.39v4.794H0v-4.794c0-.675.088-.968.43-1.31.247-.248.703-.439
 1.278-.439.464 0 .909.154 1.192.438.249.25.385.505.599 1.311zM22.575
 15.196l-1.591-4.98a.415.415 0 00-.06-.132.226.226 0
 00-.186-.082.226.226 0 00-.185.082.414.414 0 00-.06.132l-1.591
 4.98h-1.425l1.739-5.44c.09-.283.22-.524.384-.684.282-.275.614-.419
 1.138-.419.525 0 .857.144 1.139.42.164.16.294.4.384.683L24
 15.196h-1.425zM15.531 15.196c.903 0 1.344-.192
 1.692-.538.385-.383.569-.802.569-1.427
 0-.553-.202-1.064-.51-1.37-.403-.4-.903-.527-1.719-.527h-1.142c-.436
 0-.61-.053-.748-.188-.094-.093-.139-.23-.139-.393
 0-.168.04-.334.156-.448.103-.1.243-.147.511-.147h3.301V8.804h-3.049c-.903
 0-1.343.192-1.691.538-.385.383-.57.802-.57 1.427 0 .553.203 1.064.51
 1.37.404.4.904.527 1.72.527h1.141c.437 0
 .61.053.748.188.095.093.14.23.14.393 0
 .169-.041.335-.157.448-.102.1-.242.147-.51.147h-3.405l-1.306-4.086c-.09-.283-.22-.524-.384-.684-.282-.275-.615-.419-1.139-.419s-.857.144-1.138.42c-.165.16-.294.4-.385.683l-1.738
 5.44h1.424l1.592-4.98a.415.415 0 01.06-.132.226.226 0
 01.185-.082c.082 0 .142.028.186.082a.413.413 0 01.06.132l1.591
 4.98h4.144z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.nasa.gov/multimedia/guidelines/in'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:NASA_'''

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
