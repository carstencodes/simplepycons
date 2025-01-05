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


class RtlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rtl"

    @property
    def original_file_name(self) -> "str":
        return "rtl.svg"

    @property
    def title(self) -> "str":
        return "RTL"

    @property
    def primary_color(self) -> "str":
        return "#FA002E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RTL</title>
     <path d="M0 9.889v4.222h7.498V9.89H0zm8.25
 0v4.222h7.5V9.89h-7.5zm8.252
 0v4.222H24V9.89h-7.498zm-14.365.966H4.12c.61 0 .945.275.945.733 0
 .397-.254.662-.691.723l.977.824h-.754l-.926-.795H2.656v.795h-.52v-2.28zm8.281
 0h3.164v.448H12.26v1.832h-.52v-1.832h-1.322v-.448zm8.414
 0h.518v1.832h2.32v.448h-2.838v-2.28zm-16.176.428v.631H4.06c.325 0
 .478-.103.478-.316 0-.214-.153-.315-.478-.315H2.656z" />
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
