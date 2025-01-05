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


class LinkerdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linkerd"

    @property
    def original_file_name(self) -> "str":
        return "linkerd.svg"

    @property
    def title(self) -> "str":
        return "Linkerd"

    @property
    def primary_color(self) -> "str":
        return "#2BEDA7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linkerd</title>
     <path d="M22.329 5.04v9.034l1.666.964V6.004l-1.666-.964ZM0
 15.038l1.666-.964V5.04L0 6.004v9.034Zm8.165-.089 7.665
 4.424V17.45l-7.176-4.142-.489.282v1.359Zm8.105
 6.989-8.105-4.681v1.923l2.164 1.25-2.604 1.503a.263.263 0 0 0 0
 .454l1.27.737 3-1.73 3 1.73
 1.27-.737c.178-.093.178-.35.005-.449Zm6.059-11.511v8.012c0
 .202.218.331.396.227l1.142-.657a.267.267 0 0 0
 .133-.228V9.468l-1.671.959Zm-3.271 10.354 1.072-.623a.39.39 0 0 0
 .198-.341v-8.233l-1.666.963v8.012c0 .198.218.326.396.222Zm-4.063
 2.348 1.537-.885a.265.265 0 0 0
 .134-.227v-8.318l-1.671.964v8.466Zm-7.532-.89L9
 23.124v-8.461l-1.666-.964v8.313c0 .094.05.183.129.227Zm-3.598-2.076
 1.072.623a.265.265 0 0 0 .396-.227v-8.017l-1.666-.963v8.238c0
 .144.074.277.198.346ZM.198 18.048l1.072.623a.265.265 0 0 0
 .396-.228v-8.016L0 9.468v8.239c0 .138.074.267.198.341ZM23.995
 6.004l-1.666-.964-3 1.73-1.996-1.152 2.604-1.502a.264.264 0 0 0
 0-.455l-1.077-.623a.403.403 0 0 0-.395 0l-2.803
 1.616-1.996-1.151L16.27 2a.263.263 0 0 0 0-.454L15.193.923a.405.405 0
 0 0-.396 0l-2.802 1.616L9.193.923a.405.405 0 0 0-.396
 0l-1.077.623a.263.263 0 0 0 0 .454l14.6 8.432 1.665-.964-3-1.73
 3.01-1.734ZM5.135 3.038l-1.072.623a.264.264 0 0 0 0 .455l14.599 8.431
 1.666-.963L5.53 3.038a.403.403 0 0 0-.395 0ZM0 6.004l3 1.729-3 1.735
 1.671.959 2.995-1.73 2.001 1.157-3 1.73 1.666.963 3-1.734 1.996
 1.156-3 1.73L9 14.663l2.995-1.735 3 1.735 1.666-.964L1.666 5.04 0
 6.004Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cncf-branding.netlify.app/projects/li'''

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
