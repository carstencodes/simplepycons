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


class FujifilmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fujifilm"

    @property
    def original_file_name(self) -> "str":
        return "fujifilm.svg"

    @property
    def title(self) -> "str":
        return "Fujifilm"

    @property
    def primary_color(self) -> "str":
        return "#FB0020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fujifilm</title>
     <path d="M18.288 10v3.129c0 .204.096.313.3.313h1.034v.352c0
 .04-.028.068-.068.068h-1.672c-.518
 0-.6-.284-.6-.544v-3.1c0-.148.056-.216.232-.216h.774m-1.916 0v3.656c0
 .164-.068.204-.204.204h-.788v-3.655c0-.125.04-.205.216-.205h.776M0
 10.532c0-.3 0-.53.49-.53h2.12v.366c0
 .028-.012.054-.054.054H1.28c-.162
 0-.244.083-.244.26v.979h1.496v.393c0
 .04-.028.054-.056.054h-1.44v1.55c0
 .15-.082.204-.246.204H0v-3.33m4.148-.531v2.95c0
 .26.04.434.216.53.232.136.64.136.884 0
 .164-.096.232-.244.232-.53v-2.76c0-.122.04-.19.218-.19h.774v2.853c0
 .667-.42.94-.788 1.035a3.592 3.592 0 0 1-1.7
 0c-.558-.164-.816-.49-.816-1.035v-2.663c0-.122.04-.204.19-.204h.79M22.872
 10c-.19 0-.314.094-.354.272l-.626 2.663h-.014L21.212 10h-.884c-.176
 0-.23.08-.23.23v3.644h.38c.054 0 .08-.026.08-.094v-3.06h.056l.802
 3.14h.53c.204 0 .272-.08.328-.272l.72-2.868h.054v3.14h.708c.176 0
 .244-.069.244-.23V10h-1.128m-11.708 2.093h-.992v1.767h.788c.136 0
 .204-.04.204-.205v-1.562m-.054-.747c.04-.028.054-.056.054-.11V10h-.776c-.176
 0-.216.08-.216.204v1.875l.938-.733m-3.4
 2.216c.436-.055.572-.314.572-.695v-2.663c0-.164.08-.204.19-.204h.788v2.513c0
 .612-.136.927-.49 1.198-.19.136-.516.3-1.25.3-.408
 0-.6-.028-.626-.028-.04-.014-.054-.028-.054-.056v-.326c.204-.014.584
 0 .87-.04M12.674 10c-.49 0-.49.244-.49.53v.992c0
 .028-.014.028-.014.04l-.68.532h.694v1.766h.788c.164 0
 .244-.054.244-.204v-1.562h1.442c.028 0
 .054-.014.054-.056v-.394h-1.496v-.98c0-.176.082-.256.26-.256h1.278c.04
 0 .054-.028.054-.056V10h-2.134" />
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
