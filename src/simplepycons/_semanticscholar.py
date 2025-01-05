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


class SemanticScholarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "semanticscholar"

    @property
    def original_file_name(self) -> "str":
        return "semanticscholar.svg"

    @property
    def title(self) -> "str":
        return "Semantic Scholar"

    @property
    def primary_color(self) -> "str":
        return "#1857B6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Semantic Scholar</title>
     <path d="M24 8.609c-.848.536-1.436.83-2.146 1.245-4.152
 2.509-8.15 5.295-11.247 8.981l-1.488 1.817-4.568-7.268c1.021.814
 3.564 3.098 4.603 3.599l3.356-2.526c2.336-1.644 8.946-5.226
 11.49-5.848ZM8.046
 15.201c.346.277.692.537.969.744.761-3.668.121-7.613-1.886-11.039
 3.374-.052 6.731-.087 10.105-.139a14.794 14.794 0 0 1 1.298
 5.295c.294-.156.588-.294.883-.433-.104-1.868-.641-3.91-1.662-6.263-4.602-.018-9.188-.018-13.79-.018
 2.993 3.547 4.36 7.839 4.083
 11.853Zm-.623-.484c.087.086.191.155.277.225-.138-3.409-1.419-6.887-3.824-9.881H1.73c3.098
 2.855 4.984 6.299 5.693
 9.656Zm-.744-.658c.104.087.208.173.329.277-.9-2.526-2.492-5.018-4.741-7.198H0c2.89
 2.076 5.122 4.481 6.679 6.921Z" />
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
