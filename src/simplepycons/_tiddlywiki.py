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


class TiddlywikiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tiddlywiki"

    @property
    def original_file_name(self) -> "str":
        return "tiddlywiki.svg"

    @property
    def title(self) -> "str":
        return "TiddlyWiki"

    @property
    def primary_color(self) -> "str":
        return "#111111"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TiddlyWiki</title>
     <path d="m12 0 10.23 6v12L12 24 1.77 18V6L12 0zm3.961
 17.889.154-.02c.113-.043.22-.081.288-.19.227-.329-.357-.462-.566-.827-.209-.364-1.071-2.364-.418-2.924s1.359-.79
 1.629-1.315c.117-.236.238-.475.269-.742.159.132.283.255.497.262.567.036
 1.054-.658
 1.307-1.315.135-.404.244-.832.218-1.226-.069-.76.013-1.582.62-2.087-.599.302-1.167.69-1.845.789-.374-.114-.75-.216-1.147-.2-.194-.253-.456-.727-.797-.782-.58.208-.597
 1.105-.842 2.321a5.351 5.351 0 0
 0-1.154-.193c-.54-.035-1.42.134-2.038.116-.619-.018-1.836-.562-2.849-.445-.407.05-.817.12-1.195.291-.231.105-.565.421-.733.468-1.69.473-4.442.453-3.879-2.102.044-.196.056-.373-.03-.417-.11-.055-.17.06-.234.187-.985
 2.138.764 3.514 2.752 3.52.625-.048.324-.007.904-.118l-.015.082a1.87
 1.87 0 0 0 .865 1.718c-.27.771-.805 1.389-1.173 2.097.138.881 1.031
 2.057 1.4 2.225.326.147 1.036.149
 1.2-.089.059-.111.02-.351-.044-.474.277.308.651.736
 1.013.942.217.104.434.17.677.18l.31-.016c.154-.033.336-.058.44-.195.116-.2.007-.756-.476-.796-.483-.04-.795-.222-1.24-.882-.365-.638.077-1.517.226-2.145.765.123
 1.535.22 2.31.222.336-.017.67-.03 1.001-.093.106.27.402 1.025.404
 1.239.007.601-.219 1.205-.121
 1.807.06.177.005.512.35.526l.388.018.267-.008c.341.573.637.572
 1.307.591zm-7.518-1.66-.063-.056c-.184-.198-.66-.544-.572-.865.075-.238.213-.457.323-.683l-.004.023c-.02.282-.059.56.032.837.278.228.663.59.918.837-.138-.038-.4-.117-.53-.066l-.104-.026z"
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
