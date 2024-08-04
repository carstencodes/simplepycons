#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class CkeditorFourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ckeditor4"

    @property
    def original_file_name(self) -> "str":
        return "ckeditor4.svg"

    @property
    def title(self) -> "str":
        return "CKEditor 4"

    @property
    def primary_color(self) -> "str":
        return "#0287D0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CKEditor 4</title>
     <path d="M16.1237 3.7468a4.5092 4.5092 0 0 0-.469 2.009c0 2.5006
 2.0271 4.5278 4.5278 4.5278a4.447 4.447 0 0 0
 .0967-.001v6.3413a2.1307 2.1307 0 0 1-1.0654 1.8453l-8.0089
 4.6239a2.1307 2.1307 0 0 1-2.1307 0l-8.0088-4.624A2.1307 2.1307 0 0 1
 0 16.624V7.3761c0-.7613.4061-1.4647 1.0654-1.8453L9.0742.907a2.1307
 2.1307 0 0 1 2.1307 0zM5.733 7.9753a.5327.5327 0 0
 0-.5327.5327v.2542c0 .2942.2385.5327.5327.5327h8.9963a.5327.5327 0 0
 0 .5327-.5327V8.508a.5327.5327 0 0 0-.5327-.5327zm0 3.281a.5327.5327
 0 0 0-.5327.5326v.2542c0 .2942.2385.5327.5327.5327h6.5221a.5327.5327
 0 0 0 .5327-.5327v-.2542a.5327.5327 0 0 0-.5327-.5327zm0
 3.2809a.5327.5327 0 0 0-.5327.5327v.2542c0
 .2942.2385.5326.5327.5326h8.9963a.5327.5327 0 0 0
 .5327-.5326v-.2542a.5327.5327 0 0
 0-.5327-.5327zm14.5383-5.1414c-2.0593 0-3.7287-1.6694-3.7287-3.7288
 0-2.0593 1.6694-3.7287 3.7287-3.7287S24 3.6077 24 5.667c0
 2.0594-1.6694 3.7288-3.7288
 3.7288zm.6347-2.7825h.393v-.5904h-.397V4.139h-.8144l-1.1668
 1.8623v.612H20.27v.5991h.636zm-.632-1.7277v1.1373h-.6928l.6807-1.1373Z"
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
        return '''https://github.com/ckeditor/ckeditor4/blob/7d'''

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
