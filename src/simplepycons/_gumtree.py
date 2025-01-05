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


class GumtreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gumtree"

    @property
    def original_file_name(self) -> "str":
        return "gumtree.svg"

    @property
    def title(self) -> "str":
        return "Gumtree"

    @property
    def primary_color(self) -> "str":
        return "#72EF36"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gumtree</title>
     <path d="M18.846 6.582a.698.698 0 0 1-.333-.599C18.181 2.66 15.39
 0 12 0 8.609 0 5.75 2.593 5.485 5.983a.796.796 0 0 1-.332.599C3.49
 7.778 2.36 9.707 2.36 11.9c0 2.991 2.061 5.584 4.853
 6.316.465.133.998.2
 1.13.066.333-.2.798-1.862.599-2.194-.134-.2-.533-.399-1.064-.532-1.662-.465-2.86-1.928-2.86-3.723
 0-.997.4-1.861.998-2.592a2.927 2.927 0 0 1 .998-.798c.73-.4 1.13-1.13
 1.13-1.928 0-.4.066-.798.2-1.196.531-1.53 1.927-2.66 3.656-2.66 1.728
 0 3.125 1.13 3.656 2.66.132.399.2.798.2 1.196 0 .798.397 1.529 1.13
 1.928.398.2.664.465.997.798a3.918 3.918 0 0 1 .997 2.592 3.859 3.859
 0 0 1-3.855 3.856c-2.46 0-4.388 1.995-4.388 4.455v2.526c0
 .465.066.997.2 1.13.266.267 1.995.267 2.26 0
 .133-.133.2-.665.2-1.13v-2.593c0-.93.797-1.728 1.728-1.728 3.59 0
 6.515-2.925 6.515-6.515-.002-2.128-1.133-4.056-2.794-5.252z" />
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
