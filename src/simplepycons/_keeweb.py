#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class KeewebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "keeweb"

    @property
    def original_file_name(self) -> "str":
        return "keeweb.svg"

    @property
    def title(self) -> "str":
        return "KeeWeb"

    @property
    def primary_color(self) -> "str":
        return "#528BFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KeeWeb</title>
     <path d="M6.4138
 24c-.2293-.0004-.4838-.0966-.7462-.2342-.5598-.2937-.9436-.665-.6231-1.2759l7.786-14.8424a58
 58 0 0 1-.2224-.1157C9.8007 6.059 8.5551 3.8816 9.5635
 1.9594c1.159-2.2094 4.7486-2.6104 8.0176-.8956 3.269 1.7149 4.9794
 4.8961 3.8204 7.1056-.9968 1.9001-3.5993 2.0696-6.2161.6968a85 85 0 0
 0-.3215-.1672L7.0716
 23.5533c-.1703.3246-.3979.4471-.6578.4467m-1.4335-3.1798-.1474-.0773-.0328-.0171-1.9943-1.0463-.4808-.2522a.1664.1664
 0 0 1-.0701-.2247l.6312-1.2032a.1665.1665 0 0 1
 .2235-.0707l.0013.0006.9615.5044a.1665.1665 0 0 0
 .2247-.0701l.6312-1.2031a.1665.1665 0 0
 0-.0701-.2248l-.4808-.2522-.4807-.2522a.1664.1664 0 0
 1-.0701-.2247l.6311-1.2033a.1664.1664 0 0 1 .2247-.07l.4809.2522
 1.2514.6565.7757.4069.001.0005.1465.0768-.663
 1.2636-.0456.087v.0002l-.9405 1.7927-.0957.1823-.5355
 1.0208-.0003.0007zm3.1515-6.0076-.1474-.0774-.7002-.3673-.5529-.29a.1665.1665
 0 0 1-.0702-.2247l.6313-1.2032a.1665.1665 0 0 1
 .2247-.0702l.5529.2901.7002.3674.001.0004.1465.077-.0774.1473-.3155.6016-.3156.6016-.0004.0006zm10.302-7.121c.4153.0008.74-.1664.9557-.5777.6575-1.2533-.5588-3.1869-2.7166-4.3188s-4.44-1.0336-5.0974.2197
 1.1712 2.0762 3.329 3.2082c1.4498.7605 2.6792 1.467 3.5294 1.4687" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/keeweb/keeweb/blob/44432eb'''

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