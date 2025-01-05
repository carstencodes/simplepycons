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


class ConfluenceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "confluence"

    @property
    def original_file_name(self) -> "str":
        return "confluence.svg"

    @property
    def title(self) -> "str":
        return "Confluence"

    @property
    def primary_color(self) -> "str":
        return "#172B4D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Confluence</title>
     <path d="M.87 18.257c-.248.382-.53.875-.763 1.245a.764.764 0 0 0
 .255 1.04l4.965 3.054a.764.764 0 0 0
 1.058-.26c.199-.332.454-.763.733-1.221 1.967-3.247 3.945-2.853
 7.508-1.146l4.957 2.337a.764.764 0 0 0
 1.028-.382l2.364-5.346a.764.764 0 0 0-.382-1 599.851 599.851 0 0
 1-4.965-2.361C10.911 10.97 5.224 11.185.87 18.257zM23.131
 5.743c.249-.405.531-.875.764-1.25a.764.764 0 0
 0-.256-1.034L18.675.404a.764.764 0 0
 0-1.058.26c-.195.335-.451.763-.734 1.225-1.966 3.246-3.945 2.85-7.508
 1.146L4.437.694a.764.764 0 0 0-1.027.382L1.046 6.422a.764.764 0 0 0
 .382 1c1.039.49 3.105 1.467 4.965 2.361 6.698 3.246 12.392 3.029
 16.738-4.04z" />
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
