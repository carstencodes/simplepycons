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


class ClineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cline"

    @property
    def original_file_name(self) -> "str":
        return "cline.svg"

    @property
    def title(self) -> "str":
        return "Cline"

    @property
    def primary_color(self) -> "str":
        return "#18181B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cline</title>
     <path d="m23.365
 13.556-1.442-2.895V8.994c0-2.764-2.218-5.002-4.954-5.002h-2.464c.178-.367.276-.779.276-1.213A2.77
 2.77 0 0 0 12.018 0a2.77 2.77 0 0 0-2.763 2.779c0 .434.098.846.276
 1.213H7.067c-2.736 0-4.954 2.238-4.954 5.002v1.667L.64
 13.549c-.149.29-.149.636 0 .927l1.472 2.855v1.667C2.113 21.762 4.33
 24 7.067 24h9.902c2.736 0 4.954-2.238
 4.954-5.002V17.33l1.44-2.865c.143-.286.143-.622.002-.91m-12.854
 2.36a2.27 2.27 0 0 1-2.261 2.273 2.27 2.27 0 0
 1-2.261-2.273v-4.042A2.27 2.27 0 0 1 8.249 9.6a2.267 2.267 0 0 1
 2.262 2.274zm7.285 0a2.27 2.27 0 0 1-2.26 2.273 2.27 2.27 0 0
 1-2.262-2.273v-4.042A2.267 2.267 0 0 1 15.535 9.6a2.267 2.267 0 0 1
 2.261 2.274z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cline.bot/assets/branding/logos/cline'''

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
