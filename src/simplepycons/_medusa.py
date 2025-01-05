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


class MedusaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "medusa"

    @property
    def original_file_name(self) -> "str":
        return "medusa.svg"

    @property
    def title(self) -> "str":
        return "Medusa"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Medusa</title>
     <path d="M20.325 3.8958 14.8913.7692a5.7283 5.7283 0 0 0-5.7342
 0L3.6983 3.8958C1.9455 4.9213.8437 6.8223.8437 8.8484v6.2783c0 2.051
 1.1018 3.927 2.8546 4.9526l5.4337 3.1515a5.7283 5.7283 0 0 0 5.7343
 0l5.4338-3.1515c1.7778-1.0256 2.8545-2.9015
 2.8545-4.9526V8.8484c.0501-2.026-1.0517-3.927-2.8296-4.9526Zm-8.3133
 13.6821c-3.08 0-5.584-2.5013-5.584-5.5778 0-3.0767 2.504-5.578
 5.584-5.578 3.08 0 5.609 2.5013 5.609 5.578 0 3.0765-2.504
 5.5778-5.609 5.5778z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/medusajs/medusa/blob/5b91a'''

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
