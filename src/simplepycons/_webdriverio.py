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


class WebdriverioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webdriverio"

    @property
    def original_file_name(self) -> "str":
        return "webdriverio.svg"

    @property
    def title(self) -> "str":
        return "WebdriverIO"

    @property
    def primary_color(self) -> "str":
        return "#EA5906"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WebdriverIO</title>
     <path d="M1.875 0C0.836 0 0 0.836 0 1.875v20.25C0 23.164 0.836 24
 1.875 24h20.25C23.164 24 24 23.164 24 22.125V1.875C24 0.836 23.164 0
 22.125 0ZM2.25 6H3V18H2.25ZM9.335 6H10.125L5.29 18H4.499ZM16.125
 6c3.314 0 6 2.686 6 6 0 3.314-2.686 6-6 6-3.314 0-6-2.686-6-6 0-3.314
 2.686-6 6-6zm0 0.75c-2.899 0-5.25 2.351-5.25 5.25 0 2.899 2.351 5.25
 5.25 5.25 2.899 0 5.25-2.351 5.25-5.25 0-2.899-2.351-5.25-5.25-5.25z"
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
