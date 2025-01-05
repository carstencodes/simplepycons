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


class McafeeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mcafee"

    @property
    def original_file_name(self) -> "str":
        return "mcafee.svg"

    @property
    def title(self) -> "str":
        return "McAfee"

    @property
    def primary_color(self) -> "str":
        return "#C01818"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>McAfee</title>
     <path d="M12 4.8233L1.5793 0v19.1767L12
 24l10.4207-4.8233V0zm6.172 11.626l-6.143
 2.8428-6.1438-2.8429V6.6894l6.1439 2.8418 6.1429-2.8418z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.mcafee.com/enterprise/en-us/about'''

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
