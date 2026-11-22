#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class MarkoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "marko"

    @property
    def original_file_name(self) -> "str":
        return "marko.svg"

    @property
    def title(self) -> "str":
        return "Marko"

    @property
    def primary_color(self) -> "str":
        return "#CC0067"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Marko</title>
     <path d="M5.0205 9.7555a.45.45 0 0 0 0-.4565L3.4434
 6.5946a.2421.2421 0 0 0-.4288 0L.0612 11.7752a.457.457 0 0 0 0
 .4565l3.5828 6.1421a.457.457 0 0 0 .4012.2282h3.0434a.3036.3036 0 0 0
 .2628-.4634l-3.5967-6.1421Zm2.8635 2.2479h3.32a.462.462 0 0 0
 .4012-.2351l1.1136-2.0128c.083-.1383.0761-.3113
 0-.4565l-1.577-2.6975a.2421.2421 0 0 0-.4289 0L9.5371
 8.6972l-1.7984-3.071a.457.457 0 0 0-.3942-.2282H4.308a.3043.3043 0 0
 0-.2628.4634l3.4445 5.9138a.47.47 0 0 0
 .4012.2282Zm7.4217-.0069-3.5829
 6.1421c-.1176.2075.0277.4565.2628.4565h3.0572a.453.453 0 0 0
 .3943-.2282l3.5967-6.1352c.083-.1383.083-.3182
 0-.4634l-3.5967-6.1421a.457.457 0 0 0-.3943-.2282h-3.0572a.3043.3043
 0 0 0-.2628.4634zm1.6046-6.5985h3.0503c.166 0
 .3113.0899.3943.2282l3.5828 6.1421c.083.1383.083.3182 0 .4634l-3.5828
 6.1352a.457.457 0 0 1-.3943.2282h-3.0503a.3043.3043 0 0
 1-.2697-.4565l3.5829-6.1421-3.5829-6.1351c-.1176-.2075.0277-.4634.2697-.4634"
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
        return '''https://github.com/marko-js/website/blob/c6f0'''

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
