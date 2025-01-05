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


class ClickhouseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clickhouse"

    @property
    def original_file_name(self) -> "str":
        return "clickhouse.svg"

    @property
    def title(self) -> "str":
        return "ClickHouse"

    @property
    def primary_color(self) -> "str":
        return "#FFCC01"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ClickHouse</title>
     <path d="M21.333 10H24v4h-2.667ZM16 1.335h2.667v21.33H16Zm-5.333
 0h2.666v21.33h-2.666ZM0
 22.665V1.335h2.667v21.33zm5.333-21.33H8v21.33H5.333Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/ClickHouse/ClickHouse/blob
/12bd453a43819176d25ecf247033f6cb1af54beb/website/images/logo-clickhou'''

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
