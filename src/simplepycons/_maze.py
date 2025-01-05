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


class MazeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maze"

    @property
    def original_file_name(self) -> "str":
        return "maze.svg"

    @property
    def title(self) -> "str":
        return "Maze"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Maze</title>
     <path d="M1.126 16.547c-1.5013-1.4881-1.5013-3.9009
 0-5.389l4.0778-4.042c1.2692-1.258 3.205-1.4525
 4.6803-.5836.4564.2687.4524.8852.077
 1.2573-.3753.372-.988.34-1.4975.1923-.6524-.1891-1.386-.0287-1.9006.4813l-4.0777
 4.0419a1.8935 1.8935 0 0 0 0 2.6945c.7506.744 1.9678.744 2.7184
 0l8.1555-8.0836c1.5014-1.4882 3.9355-1.4882 5.437 0l4.0778
 4.0418c1.5013 1.4881 1.5013 3.901 0 5.389-1.5014 1.4882-3.9356
 1.4882-5.437 0l-1.3593-1.3472-1.699 1.684c-1.2692 1.258-3.205
 1.4526-4.6804.5837-.4563-.2687-.4523-.8852-.077-1.2573.3754-.372.988-.34
 1.4975-.1923.6524.1892 1.386.0287
 1.9006-.4813l1.7476-1.7322c.724-.7175 1.8975-.7175 2.6214 0l1.4078
 1.3954c.7507.744 1.9678.744 2.7186 0a1.8936 1.8936 0 0 0
 0-2.6945l-4.0779-4.0419c-.7507-.744-1.9678-.744-2.7185 0L6.563
 16.5471c-1.5014 1.4882-3.9356 1.4881-5.437 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://mazedesign.notion.site/Press-Kit-421d'''

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
