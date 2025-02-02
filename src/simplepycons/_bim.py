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


class BimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bim"

    @property
    def original_file_name(self) -> "str":
        return "bim.svg"

    @property
    def title(self) -> "str":
        return "BIM"

    @property
    def primary_color(self) -> "str":
        return "#EB1928"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BIM</title>
     <path d="M3.327 6.3015c-1.8378 0-3.3266 1.4908-3.3266
 3.3283v4.7424c0 1.8375 1.4888 3.3263 3.3265 3.3263h17.347c1.8376 0
 3.3265-1.4888
 3.3265-3.3263V9.6298c0-1.8375-1.4889-3.3283-3.3265-3.3283H12.353L11.06
 8.1922 9.7863 6.3015Zm1.5742 2.1896c.8137-.0085 1.57.0699
 2.01.2422.7978.3017 1.254.96 1.293 1.8067.0294.612-.2962 1.1623-.791
 1.5801.5608.3311.9783.8269.9649 1.5392-.0257 1.2596-1.2067
 2.0391-3.3362
 1.9903-1.1473-.0269-1.7047-.0285-2.3694-.1739V8.6395c1.1595-.1564
 1.288-.14 2.2287-.1484Zm9.5223.1113h1.9903l1.2833 3.2247
 1.2735-3.2247h2.0511l.5507 6.8675h-1.9707l-.1446-3.9123-1.7716
 3.8986-1.6466-3.885-.3418
 3.8987h-2.0158Zm-4.4732.0234h2.0901v6.8675h-2.09Zm-5.2347
 1.4298v1.4532h.8086a.7257.7257 0 0 0
 .7266-.7266c0-.4008-.2965-.7266-.7266-.7266zm0
 2.7872v1.1973h.7793c.4105.0232.9576-.1498.963-.586-.0245-.4923-.5244-.637-.9337-.6113z"
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
        return '''https://commons.wikimedia.org/wiki/File:Bim_('''

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
