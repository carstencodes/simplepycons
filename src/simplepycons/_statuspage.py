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


class StatuspageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "statuspage"

    @property
    def original_file_name(self) -> "str":
        return "statuspage.svg"

    @property
    def title(self) -> "str":
        return "Statuspage"

    @property
    def primary_color(self) -> "str":
        return "#172B4D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Statuspage</title>
     <path d="M12.008 9.597a5.623 5.623 0 1 1 0 11.245 5.623 5.623 0 0
 1 0-11.245zM.154 8.717l3.02 3.574a.639.639 0 0 0 .913.068c4.885-4.379
 10.97-4.379 15.84 0a.642.642 0 0 0 .916-.068l3.006-3.574a.646.646 0 0
 0-.075-.906c-7.1-6.204-16.462-6.204-23.555 0a.65.65 0 0 0-.065.906z"
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
        return '''https://www.atlassian.com/company/news/press-'''

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
